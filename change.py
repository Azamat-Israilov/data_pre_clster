import os

base_dir = "data_with_cluster"

for root, dirs, files in os.walk(base_dir):
    for filename in files:
        if filename.endswith(".parquet"):
            folder_name = os.path.basename(root)
            old_path = os.path.join(root, filename)

            # Пропускаем, если имя уже содержит префикс
            if filename.startswith(f"{folder_name}_"):
                continue

            new_filename = f"{folder_name}_{filename}"
            new_path = os.path.join(root, new_filename)

            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
