import os
import random
from glob import glob

# base 경로
base_dir = '/home/una/PRML-repro/data/LA-segmentation'
train_set_path = os.path.join(base_dir, 'Training Set')

# 하위 폴더 중 mri_norm2.h5가 존재하는 폴더만 수집
all_cases = sorted([
    os.path.basename(os.path.dirname(path))
    for path in glob(os.path.join(train_set_path, '*', 'mri_norm2.h5'))
])

# 셔플하고 split
random.seed(1337)  # 재현 가능하도록
random.shuffle(all_cases)

num_total = len(all_cases)
num_train = int(0.8 * num_total)
train_cases = all_cases[:num_train]
test_cases = all_cases[num_train:]

# 리스트 파일 생성
with open(os.path.join(base_dir, 'train.list'), 'w') as f:
    for case in train_cases:
        f.write(case + '\n')

with open(os.path.join(base_dir, 'test.list'), 'w') as f:
    for case in test_cases:
        f.write(case + '\n')

print(f"[✓] Created train.list ({len(train_cases)} cases)")
print(f"[✓] Created test.list ({len(test_cases)} cases)")