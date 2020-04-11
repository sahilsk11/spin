from spin import *

page_content = load_cms("content.json")

def render():
    return f"""
      <html>
        {ContentContainer()}
      </html>
    """


def ContentContainer():
    container_style = f"""
      position: relative;
      width: 100%;
      height: 100%;
    """
    return f"""
    <div {style(container_style)}>
        {Haiku()}
    </div>
  """


def Haiku():
    text_style = f"""
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: Avenir;
    color: grey;
    """
    haiku = "<br>".join(page_content["lines"])
    return f"""
      <p {style(text_style)}>
        {haiku}
      </p>
      """