tasks = []

while True:
    new_task = input("追加するタスクを入力してください(終わるなら何も入力せずEnter)：")
    if new_task == "":
        break
    task_dict = {"name":new_task, "done":False}
    tasks.append(task_dict)

print("\n--- タスク一覧 ---")
for i in range(len(tasks)):
    status = "✅" if tasks[i]["done"] else ""
    print(f"{i + 1}.[{status}] {tasks[i]['name']}")

num = input("\n完了にするタスクの番号を入力してください(スキップするならEnter)：")

if num != "":
    index = int(num) - 1
    tasks[index]["done"] = True

print("\n--- 更新後のタスク一覧 ---")
for task in tasks:
    status = "✅" if task["done"] else ""
    print(f"[{status}] {task['name']}")