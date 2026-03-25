# quick_output.py

# الخطوة 1: تحديد متغيرات
accuracy = 0.87        # ممكن تغيّريها لأي رقم
run_id = "run_123abc"  # ممكن تغيّريها لأي RUN_ID

# الخطوة 2: طباعة نتائج الـ validation
print("Accuracy:", accuracy)
if accuracy < 0.85:
    print("Model failed ❌")
else:
    print("Model passed ✅")

print("Run ID:", run_id)

# الخطوة 3: محاكاة الـ Docker Build
print(f"Building Docker image for Run ID: {run_id}")
