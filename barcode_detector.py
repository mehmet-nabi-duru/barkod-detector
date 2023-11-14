import os
from PIL import Image
from pyzbar import pyzbar


def create_search_query_txt(barcodes):
    barcodes = " OR ".join(barcodes)
    try:
        with open("barcode_arama.txt", "w") as file:
            file.write(barcodes)
    except IOError as e:
        print(f"Error writing to file: {e}")

    print("Search entry created\n\n")

def main():
    items = os.listdir(os.getcwd())
    processed_files = 0
    found_barcodes = 0

    barcode_list = []

    for item in items:
        if not item.endswith((".jpg", ".jpeg", ".png")):
            continue

        try:
            image = Image.open(item).convert("L")
        except IOError as e:
            print(f"Error opening {item}: {e}")
            continue

        barcodes = pyzbar.decode(image)
        if len(barcodes) > 0:
            barcode_data = barcodes[0].data.decode("utf-8")
            try:
                with open("barcodes.txt", "a") as file:
                    file.write(barcode_data)
                    file.write("\n")
                found_barcodes += 1
                barcode_list.append(barcode_data)
            except IOError as e:
                print(f"Error writing to file: {e}")
        else:
            print(f"No barcodes found in {item}")
        
        processed_files += 1

    create_search_query_txt(barcode_list)

    print(f"Processed {processed_files} files. Found {found_barcodes} barcodes.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error when executing the main function:",e)
    else:
        print("Operations completed successfully!")

    input("Kapatmak icin ENTERa basin")
