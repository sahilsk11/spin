//import * as pageContent from "./content.json";

const pageContent = {
  "lines": [
    "Tired from old age,",
    "Forgotten like its owner,",
    "The dog longed for life."
  ]
}

function render() {
  return `
  <div>
    ${ContentContainer()}
    ${Footer()}
  </div>
  `;
}

function ContentContainer() {
  const containerStyle = `
    position: relative;
    width: 100%;
    height: 100%;
  `
  return `
    <div style="${containerStyle}">
      ${Haiku()}
    </div>
  `
}

function Haiku() {
  const textStyle = `
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: Avenir;
    color: grey;
  `
  const haiku = pageContent["lines"].join("<br>")
  return `
    <p style="${textStyle}">
      ${haiku}
    </p>
  `
}

function Footer() {
  const textStyle = `
    text-align: center;
    font-family: Avenir;
    font-size: 14px;
    font-weight: 300;
    text-decoration: none;
    color: grey;
  `
  const linkStyle = `
    color: black;
    text-decoration: none;
    font-weight: 400;
  `
  return `
  <div>
    <p style="${textStyle}">Made in ` + "⚡️" + `with <a style="${linkStyle}" href="https://github.com/sahilsk11/spin">Spin</a></p>
    ${Button()}
  </div>
  `
}

var buttonState = 0;

function Button() {
  return `
    <button onClick="setButtonState(${buttonState+1})">${buttonState}</button>
  `
}

function setButtonState(state) {
  buttonState = state;
  console.log(buttonState)
}


console.log(render());