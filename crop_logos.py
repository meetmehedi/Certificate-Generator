import os
from PIL import Image

def crop_transparent(image_path, output_path):
    if not os.path.exists(image_path):
        print(f"Skipping: {image_path} does not exist")
        return
    
    img = Image.open(image_path)
    # Check if image has alpha channel
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        # Convert to RGBA if not already
        img_rgba = img.convert('RGBA')
        bbox = img_rgba.getbbox()
        if bbox:
            cropped = img.crop(bbox)
            cropped.save(output_path)
            print(f"Cropped and saved {image_path} -> {output_path}")
            return
    
    # If no transparent channel or no bbox, just save copy
    img.save(output_path)
    print(f"Copied {image_path} -> {output_path} (no transparency box found)")

if __name__ == '__main__':
    base_dir = '/Users/md.mehedihasan/Certificate gen'
    crop_transparent(os.path.join(base_dir, 'diu logo.png'), os.path.join(base_dir, 'diu_logo_cropped.png'))
    crop_transparent(os.path.join(base_dir, 'cpc logo.png'), os.path.join(base_dir, 'cpc_logo_cropped.png'))
    crop_transparent(os.path.join(base_dir, 'department logo.png'), os.path.join(base_dir, 'department_logo_cropped.png'))
