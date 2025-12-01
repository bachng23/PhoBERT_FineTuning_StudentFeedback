import streamlit as st
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 1. Web config 
st.set_page_config(page_title="Student Feedback AI", page_icon="🎓")

st.title("🎓 Phân loại Feedback Sinh Viên")
st.write("Nhập phản hồi của sinh viên để AI phân loại cảm xúc.")

# 2. Load Model
@st.cache_resource
def load_ai_model():
    model_path = "bachng23/PhoBERT_FineTuned_Student_Feedback"
    
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSequenceClassification.from_pretrained(model_path)
        return tokenizer, model
    except Exception as e:
        st.error(f"Lỗi không tìm thấy Model: {e}")
        return None, None

# Load model
with st.spinner("Đang khởi động 'bộ não' AI..."):
    tokenizer, model = load_ai_model()

# 3. UI
text_input = st.text_area("Nội dung Feedback:", height=100, placeholder="Ví dụ: Thầy dạy hay nhưng bài tập khó quá...")

btn_predict = st.button("🔍 Phân tích ngay")

# 4. Button Function
if btn_predict:
    if not text_input.strip():
        st.warning("Bạn chưa nhập nội dung nào cả!")
    else:
        if tokenizer is None or model is None:
            st.error("Model chưa được load thành công. Kiểm tra lại đường dẫn folder.")
        else:
            # --- Start Predicting ---
            inputs = tokenizer(text_input, return_tensors="pt", truncation=True, max_length=256)
            
            with torch.no_grad():
                outputs = model(**inputs)
            
            # Calculate Prob (Softmax)
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
            probs_list = probs[0].tolist()
            
            # Take the highest prob index
            pred_idx = torch.argmax(probs).item()
            
            # Mapping
            labels_map = {0: "Tiêu cực 😡", 1: "Trung tính 😐", 2: "Tích cực 😄"}
            colors_map = {0: "red", 1: "orange", 2: "green"}
            
            result_text = labels_map[pred_idx]
            confidence = probs_list[pred_idx]

            # --- Show Result ---
            st.markdown("---")
            st.subheader(f"Kết quả: :{colors_map[pred_idx]}[{result_text}]")
            st.caption(f"Độ tin cậy: {confidence:.2%}")
            st.write("Chi tiết điểm số:")
            col1, col2, col3 = st.columns(3)
            col1.metric("Tiêu cực", f"{probs_list[0]:.2%}")
            col2.metric("Trung tính", f"{probs_list[1]:.2%}")
            col3.metric("Tích cực", f"{probs_list[2]:.2%}")