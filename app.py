# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
# app.py
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f'Đã thêm công việc: "{task_name}"')

def list_tasks():
    """Duyệt và in ra tất cả các công việc có đánh số thứ tự."""
    if not tasks:
        print("Chưa có công việc nào.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    # Ví dụ thêm vài công việc để kiểm thử
    add_task("Học bài Git")
    add_task("Làm bài tập")
    # Gọi hàm liệt kê công việc
    print("\nDanh sách công việc hiện tại:")
    list_tasks()
