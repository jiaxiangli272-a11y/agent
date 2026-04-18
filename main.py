import os
import matplotlib.pyplot as plt
from PIL import Image

# 1. 基础路径设置 (Linux环境，严格区分大小写)
base_dir = os.path.expanduser("/data2/ljx/images")

# 2. 定义行和列
folders = ["sleepmark", "hidden", "MBRS", "stablesignature", "yu1", "yu2"]
row_labels = ["SleeperMark", "Hidden", "MBRS", "StableSignature", "YU1", "YU2"]

files = ["water.png", "VAE.png", "WEvade.png", "unmark.png", "our.png"]
col_labels = ["w_image", "VAEAttack", "Wevade", "Unmarker", "Our"]

# 🔥 新增：定义统一的图片大小，防止因个别图片分辨率不同导致排版错乱、间隙变大
TARGET_SIZE = (256, 256)

fig, axes = plt.subplots(nrows=len(folders), ncols=len(files), figsize=(12, 10))
fig.subplots_adjust(wspace=0.0, hspace=0.0)

for i, folder_name in enumerate(folders):
    for j, file_name in enumerate(files):
        ax = axes[i, j]

        # 🔥 强化：彻底清理坐标轴刻度和标签，哪怕没有图也不会出现 0.00~1.00 的数字
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.tick_params(axis='both', which='both', length=0)

        # 保留浅灰色边框模拟表格线
        for spine in ax.spines.values():
            spine.set_edgecolor('#DDDDDD')
            spine.set_linewidth(1)

        img_path = os.path.join(base_dir, folder_name, file_name)

        try:
            # 🔥 强化：转为 RGB (防止 PNG 透明通道报错)，并统一强制缩放到相同尺寸
            img = Image.open(img_path).convert('RGB')
            img = img.resize(TARGET_SIZE)
            ax.imshow(img)
        except Exception as e:
            # 如果某张图片找不到，画一个显眼的红色提示
            ax.text(0.5, 0.5, 'Missing', ha='center', va='center', color='red', fontsize=12, fontweight='bold')
            print(f"❌ 读取失败: {img_path} | 原因: {e}")

        # 5. 设置第一行的列标签
        if i == 0:
            ax.set_title(
                col_labels[j],
                fontsize=14,
                fontweight='bold',
                pad=15,
                bbox=dict(facecolor='#DDF0FF', edgecolor='none', pad=10)
            )

        # 6. 设置第一列的行标签
        if j == 0:
            ax.set_ylabel(
                row_labels[i],
                fontsize=14,
                fontweight='bold',
                rotation=0,
                labelpad=40,
                ha='right',
                va='center'
            )

# 7. 保存结果
output_path = os.path.join(base_dir, "combined_result.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✅ 图片拼接完成！已保存至: {output_path}")

# 🔥 新增：防止 Linux 服务器环境没有 Display 图形界面导致报错崩溃
try:
    plt.show()
except Exception:
    pass