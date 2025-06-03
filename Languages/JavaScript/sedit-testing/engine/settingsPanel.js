class SettingsPanel extends HTMLElement {
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
        <form>
          <!-- Block Specific settings start here -->
          <fieldset>
            <label for="includeContent">Include Content?</label>
            <input type="checkbox" name="includeContent" id="includeContent">
          </fieldset>
          <!-- Block Specific settings end here -->
        </form>
      </details>
    `
  }
}

customElements.define('settings-panel', SettingsPanel);
