export const globalCSS = `
.editable, .field{
    position: relative;
    min-width:2px;
    margin:0.25rem; /* Need some space to be able to edit*/
    padding:0.25rem;
}
.editable:hover{
    border: 5px dashed #7c50ff;
}
.field:hover{
    border: 5px dashed #e750ff;
}
`
export function initializeComponent(shadowDom){
    shadowDom.innerHTML = `<style>${globalCSS}</style>` + shadowDom.innerHTML

    // Set All fields to editable
    Array.from(shadowDom.querySelectorAll(".field")).forEach((el) =>{
        el.contentEditable = true
    })
    // Add Settings icon to edtiable blocks
    Array.from(shadowDom.querySelectorAll(".editable")).forEach((el) =>{
        el.innerHTML = "<settings-panel></settings-panel>"+ el.innerHTML
    })
}

export class SettingsPanel extends HTMLElement {
//   static get observedAttributes() {
//     return ['block-id']; // Watch for changes to this attribute
//   }
  
  constructor() {
    super();
    const shadow = this.attachShadow({ mode: 'open' });

    shadow.innerHTML = `
      <style>
        details.settings {
          position: absolute;
          text-align: right;
          top: 0.3rem;
          right: 0.3rem;
          width: fit-content;
          font-size: 2rem;
          background: white;
          border-radius: 0.4rem;
          padding: 0.3rem;
          z-index: 1000;
        }

        summary {
          cursor: pointer;
          display: inline;
          list-style: none;
        }

        details[open]::before {
          content: "Block Settings";
          text-decoration: underline;
          font-weight: bold;
          font-size: 1rem;
          display: inline;
          margin-bottom: 0.5rem;
        }

        summary::-webkit-details-marker,
        summary::marker {
          display: none;
        }

        form {
          padding: 1rem;
          font-size: 1rem;
          display: flex;
          flex-direction: column;
        }
        
        fieldset{
            border-radius:.5rem;
            box-shadow: 1px 1px 1px black;
        }

        label {
          margin-bottom: 0.5rem;
        }
      </style>

      <details class="settings">
        <summary>⚙️</summary>
        <form action="">
          <fieldset>
            <label for="includeContent">Include Content?</label>
            <input type="checkbox" name="includeContent" id="includeContent">
          </fieldset>
        </form>
      </details>
    `
  }
}
window.initializeEngine = ()=>{
    console.log("Initializing engine")
    if (!customElements.get("settings-panel")){
        console.log("Engine not initialized, initializing")
        customElements.define('settings-panel', SettingsPanel);
    }
}

