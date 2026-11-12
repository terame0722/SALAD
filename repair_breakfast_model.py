
import zipfile
import shutil

source = "results/breakfast_box/autoencoder_final.pth"
destination = "results/breakfast_box/autoencoder_repaired.pth"

prefix = "autoencoder_final/"

with zipfile.ZipFile(source, "r") as src:
    valid_entries = [
        item for item in src.infolist()
        if item.filename.startswith(prefix)
    ]

    print(f"Valid entries: {len(valid_entries)}")

    with zipfile.ZipFile(
        destination, "w", allowZip64=True
    ) as dst:
        for item in valid_entries:
            with src.open(item) as input_file:
                with dst.open(item, "w", force_zip64=True) as output_file:
                    shutil.copyfileobj(input_file, output_file, 1024 * 1024)

            print("Copied:", item.filename)

print("Repair completed:", destination)
