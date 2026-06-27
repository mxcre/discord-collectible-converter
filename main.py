import json

def format_effects(effects):
    lines = []
    for e in effects:
        lines.append(
            "            { "
            f'src: "{e.get("src")}", '
            f'loop: {str(e.get("loop")).lower()}, '
            f'duration: {e.get("duration")}, '
            f'start: {e.get("start")}, '
            f'loopDelay: {e.get("loopDelay")}, '
            f'zIndex: {e.get("zIndex")}, '
            'randomizedSources: [] '
            "},"
        )
    return "\n".join(lines)


def convert(data):
    output = []

    for variant in data.get("variants", []):
        item = variant["items"][0]

        block = f"""    {{
        id: "{variant.get("sku_id")}",
        label: "{variant.get("name")}",
        staticFrameSrc: "{item.get("thumbnailPreviewSrc")}",
        thumbnailPreviewSrc: "{item.get("thumbnailPreviewSrc")}",
        reducedMotionSrc: "{item.get("reducedMotionSrc")}",
        effects: [
{format_effects(item.get("effects", []))}
        ]
    }},"""

        output.append(block)

    return "\n\n".join(output)


if __name__ == "__main__":
    with open("raw.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    result = convert(data)

    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("result.txt ok")