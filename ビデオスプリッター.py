import os
import sys
import shutil

def sort_videos(directory):
    """
    ビデオファイルをサブフォルダーに分類するスクリプト。
    各サブフォルダーには最大15個のビデオが含まれます。

    Args:
    directory (str): ビデオが含まれているディレクトリのパス。
    """

    # ビデオファイルの拡張子リスト
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv']

    # ディレクトリ内のすべてのファイルをチェック
    videos = [file for file in os.listdir(directory) if os.path.splitext(file)[1].lower() in video_extensions]

    # サブフォルダーに分類
    subfolder_count = 0
    for i, video in enumerate(videos):
        if i % 15 == 0:
            subfolder_count += 1
            subfolder_path = os.path.join(directory, f'subfolder_{subfolder_count}')
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
        
        # ビデオを新しいサブフォルダーに移動
        shutil.move(os.path.join(directory, video), subfolder_path)

    print(f"ビデオが {subfolder_count} 個のサブフォルダーに分類されました。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python script.py [ディレクトリパス]")
    else:
        sort_videos(sys.argv[1])
