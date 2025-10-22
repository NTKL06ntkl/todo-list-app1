# Khởi tạo danh sách công việc trống
tasks = []

# Thêm một công việc mới
def add_task(task_name):
    """Thêm một công việc mới vào danh sách dưới dạng dictionary"""
    task = {'name': task_name, 'completed': False}  # mỗi công việc là dictionary
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")

# Liệt kê tất cả công việc
def list_tasks():
    """Liệt kê tất cả các công việc cùng trạng thái hoàn thành"""
    if not tasks:
        print("Danh sách công việc hiện tại trống.")
    else:
        print("\nDanh sách công việc hiện tại:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")

# Đánh dấu công việc hoàn thành
def complete_task(task_index):
    """Đánh dấu một công việc là đã hoàn thành"""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"✅ Đã đánh dấu hoàn thành: {tasks[task_index]['name']}")
    else:
        print("❌ Không tồn tại công việc với số thứ tự này.")

# Thử nghiệm
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    
    # Thêm công việc mới
    add_task("Học bài Git")
    add_task("Làm bài tập")
    
    # Đánh dấu công việc đầu tiên hoàn thành
    complete_task(0)
    
    # Liệt kê danh sách công việc
    list_tasks()
def delete_task(task_index):
    """
    Xóa một công việc khỏi danh sách dựa trên chỉ số.

    Tham số:
    - task_index: số thứ tự công việc (bắt đầu từ 0)

    Nếu số thứ tự không hợp lệ, in thông báo lỗi.
    """
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"🗑️ Đã xóa công việc: {removed_task['name']}")
    else:
        print("❌ Không tồn tại công việc với số thứ tự này.")
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    
    # Thêm công việc
    add_task("Học bài Git")
    add_task("Làm bài tập")
    
    # Đánh dấu công việc hoàn thành
    complete_task(0)
    
    # Xóa một công việc (ví dụ xóa công việc thứ 2)
    delete_task(1)
    
    # Liệt kê danh sách cuối cùng
    list_tasks()

