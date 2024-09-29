from flask import Flask, jsonify
from concurrent.futures import ThreadPoolExecutor
import time
import uuid
import threading

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=5)

# 存储任务结果和事件的字典
task_results = {}
task_events = {}
lock = threading.Lock()

def task_a(task_id):
    # 模拟任务处理时间
    time.sleep(5)
    result = f"Task completed!"
    
    # 存储结果
    with lock:
        task_results[task_id] = result
        task_events[task_id].set()

@app.route('/do_task', methods=['POST'])
def do_task():
    # 生成唯一的任务标识符
    task_id = str(uuid.uuid4())
    
    # 创建事件以等待任务完成
    event = threading.Event()
    
    # 保护临界区
    with lock:
        task_events[task_id] = event
    
    # 提交任务
    executor.submit(task_a, task_id)
    
    # 等待任务完成信号
    event.wait()
    
    # 获取任务结果并移除
    result = task_results.pop(task_id)  # 获取结果并移除
    with lock:
        task_events.pop(task_id)  # 移除事件对象
    return jsonify({'task_id': task_id, 'result': result}), 200

if __name__ == '__main__':
    app.run(port=8080, debug=True)
