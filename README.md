# 🎓 Phân loại Feedback Sinh Viên bằng PhoBERT
Dự án sử dụng mô hình ngôn ngữ **PhoBERT** (VinAI) được tinh chỉnh (fine-tuned) để phân loại ý kiến phản hồi của sinh viên thành 3 nhóm cảm xúc.

## 🌟 Trải nghiệm ngay (Live Demo)

👉 **Bấm vào đây để dùng thử Web App:** **[LINK_WEB_STREAMLIT_CUA_BAN_TAI_DAY](https://share.streamlit.io/...)**

*(Chờ khoảng 30s để App khởi động lần đầu)*

---

## 🚀 Tính năng
- Phân loại văn bản tiếng Việt tự động.
- **3 Nhãn cảm xúc:**
  - 😡 **Tiêu cực (0):** Phàn nàn, chê trách.
  - 😐 **Trung tính (1):** Góp ý, nhận xét bình thường.
  - 😄 **Tích cực (2):** Khen ngợi, hài lòng.
- Giao diện trực quan, hiển thị độ tin cậy (Confidence score).

## 🛠 Công nghệ sử dụng
- **Model:** [vinai/phobert-base](https://huggingface.co/vinai/phobert-base)
- **Library:** Transformers (Hugging Face), PyTorch.
- **Web Framework:** Streamlit.
- **Deployment:** Streamlit Cloud (Frontend) + Hugging Face Hub (Model Storage).
