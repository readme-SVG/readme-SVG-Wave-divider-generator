import os
from flask import Flask, Response, request, send_file
from .wave import generate_wave_svg

app = Flask(__name__)


@app.route("/")
def index():
    html_path = os.path.join(os.path.dirname(__file__), "..", "index.html")
    return send_file(os.path.abspath(html_path))


@app.route("/wave")
def wave():
    """
    GET /wave — returns an SVG wave divider

    Parameters:
      type          sine | smooth | zigzag | bump | triangle  (default: smooth)
      width         200–2400  (default: 1200)
      height        20–200    (default: 80)
      color_top     hex, no # (default: 0d1117)
      color_bottom  hex, no # (default: 161b22)
      amplitude     1–100     (default: 20)
      frequency     0.5–8     (default: 1)
      layers        1–3       (default: 1)
      flip          true|false (default: false) — flips wave vertically
      gradient      true|false (default: false) — horizontal gradient fill
      mirror        true|false (default: false) — adds mirrored ghost layer
      opacity       0–1       (default: 1)
    """
    wave_type  = request.args.get("type", "smooth").lower()
    width      = min(max(int(request.args.get("width", 1200)), 200), 2400)
    height     = min(max(int(request.args.get("height", 80)), 20), 200)
    color_top  = "#" + request.args.get("color_top", "0d1117").lstrip("#")
    color_bot  = "#" + request.args.get("color_bottom", "161b22").lstrip("#")
    amplitude  = min(max(float(request.args.get("amplitude", 20)), 1), 100)
    frequency  = min(max(float(request.args.get("frequency", 1)), 0.5), 8)
    layers     = min(max(int(request.args.get("layers", 1)), 1), 3)
    flip       = request.args.get("flip", "false").lower() == "true"
    gradient   = request.args.get("gradient", "false").lower() == "true"
    mirror     = request.args.get("mirror", "false").lower() == "true"
    opacity    = min(max(float(request.args.get("opacity", 1)), 0.1), 1)

    svg = generate_wave_svg(
        wave_type=wave_type,
        width=width,
        height=height,
        color_top=color_top,
        color_bottom=color_bot,
        amplitude=amplitude,
        frequency=frequency,
        layers=layers,
        flip=flip,
        gradient=gradient,
        mirror=mirror,
        opacity=opacity,
    )

    return Response(
        svg,
        mimetype="image/svg+xml",
        headers={
            "Cache-Control": "public, max-age=3600",
            "Access-Control-Allow-Origin": "*",
        },
    )
