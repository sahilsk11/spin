from spin import *

page_content = load_cms("content.json")


def render():
    return f"""
      <html>
        {Head()}
        <body>
          {ContentContainer()}
          {Footer()}
        </body>
      </html>
    """


def Head():
    return f"""
      <head>
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>My App - Built with Spin</title>
          <link href="https://image.flaticon.com/icons/svg/740/740845.svg" rel="icon">
        </head>
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
    border: 1px solid red;
    """
    haiku = "<br>".join(page_content["lines"])
    return f"""
      <p {style(text_style)}>
        {haiku}
      </p>
      """


def Footer():
    text_style = f"""
      text-align: center;
      font-family: Avenir;
      font-size: 14px;
      font-weight: 300;
      text-decoration: none;
      color: grey;
    """
    link_style = f"""
      text-decoration: none;
      color: black;
      font-weight: 400;
    """
    return f"""
      <div>
        <p {style(text_style)}>Built in ⚡️with <a {style(link_style)} href="https://github.com/sahilsk11/spin">Spin</a></p>
      </div>
    """
