import torch
import time

# デバイスの設定
device_cpu = torch.device("cpu")  # CPU
device_gpu = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")  # GPU

# 大きなランダム行列を生成 (3000 x 3000)
matrix_size = 10000
a = torch.randn(matrix_size, matrix_size)
b = torch.randn(matrix_size, matrix_size)

# CPUでの計算時間を計測
a_cpu = a.to(device_cpu)
b_cpu = b.to(device_cpu)
start_time = time.time()
result_cpu = torch.matmul(a_cpu, b_cpu)  # 行列積
cpu_time = time.time() - start_time
print(f"CPUでの計算時間: {cpu_time:.4f} 秒")

# GPUでの計算時間を計測
a_gpu = a.to(device_gpu)
b_gpu = b.to(device_gpu)
torch.cuda.synchronize()  # 計測前にGPUの状態を同期
start_time = time.time()
result_gpu = torch.matmul(a_gpu, b_gpu)  # 行列積
torch.cuda.synchronize()  # 計測後もGPUの状態を同期
gpu_time = time.time() - start_time
print(f"GPUでの計算時間: {gpu_time:.4f} 秒")

# 性能比較
speedup = cpu_time / gpu_time if gpu_time > 0 else float('inf')
print(f"GPUはCPUの約 {speedup:.2f} 倍速いです！")
