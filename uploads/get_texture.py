import unreal
import re

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

for sa in selected_assets:
    if sa.get_class().get_name() == "Material":
        textures = unreal.MaterialEditingLibrary.get_used_textures(sa)
        x = []
        y = []

        for texture in textures:
            sizeX = unreal.Texture2D.blueprint_get_size_x(texture)
            x.append(sizeX)
            sizeY = unreal.Texture2D.blueprint_get_size_y(texture)
            y.append(sizeY)

            texture_path = re.match(r"<Object ('.*?')", str(texture)).group(1)
            texture_name = texture_path.split("/")[-1].split(".")[-1].strip("'")

            print(f"{texture_name}: {sizeX}x{sizeY}")

        final_sizeX = sum(x)
        final_sizeY = sum(y)

        print(f"Total texture size: {final_sizeX}x{final_sizeY}")
