import os
import shutil

def reconstruct_bins(bin_folder, output_file):
    bin_files = sorted([f for f in os.listdir(bin_folder) if f.endswith('.bin')],
                       key=lambda x: int(os.path.splitext(x)[0]))
    with open(output_file, 'wb') as outfile:
        for bin_file in bin_files:
            bin_path = os.path.join(bin_folder, bin_file)
            with open(bin_path, 'rb') as infile:
                outfile.write(infile.read())

def process_xfbin_extract_folder(extract_folder_path, original_xfbin_path):
    toc_folder = os.path.join(extract_folder_path, 'ITOC')
    if not os.path.exists(toc_folder):
        toc_folder = os.path.join(extract_folder_path, 'TOC')

    if not os.path.exists(toc_folder):
        print(f"No TOC/ITOC found in {extract_folder_path}")
        return False

    # Get original filename from the folder name
    folder_basename = os.path.basename(extract_folder_path)
    filename = folder_basename.replace("VGMT_CPK_EXTRACT_", "").replace(".xfbin", "")
    reconstructed_filename = f"{filename}_reconstructed.xfbin"
    
    reconstructed_file_path = os.path.join(os.path.dirname(original_xfbin_path), reconstructed_filename)

    # Perform the reconstruction
    reconstruct_bins(toc_folder, reconstructed_file_path)
    print(f"Reconstructed {reconstructed_filename} at {reconstructed_file_path}")

    # Clean up by removing the extraction folder
    shutil.rmtree(extract_folder_path)
    print(f"Deleted {extract_folder_path}")

    return True

def scan_and_reconstruct(base_folder):
    for root, dirs, files in os.walk(base_folder):
        for d in dirs:
            if d.startswith("VGMT_CPK_EXTRACT_") and d.endswith(".xfbin"):
                extract_folder_path = os.path.join(root, d)
                original_xfbin_name = d.replace("VGMT_CPK_EXTRACT_", "")
                original_xfbin_path = os.path.join(root, original_xfbin_name)
                
                if os.path.exists(original_xfbin_path):
                    process_xfbin_extract_folder(extract_folder_path, original_xfbin_path)
                else:
                    print(f"Warning: Original file {original_xfbin_path} not found for {extract_folder_path}")

if __name__ == "__main__":
    # Run this script from the top-level folder you want to process
    current_directory = os.path.abspath(os.path.dirname(__file__))
    scan_and_reconstruct(current_directory)

    input("All done! Press Enter to exit.")
