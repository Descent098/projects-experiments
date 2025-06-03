import { initializeComponent } from "../engine/main.js";
class Hero extends HTMLElement {
    constructor() {
        super();
        const shadow = this.attachShadow({ mode: 'open' });
        
        shadow.innerHTML = `
        <style>
            .hero{
                color: var(--primary-color);
                background:var(--secondary-color);
                height:70vh;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                border-bottom-left-radius: 1rem;
                border-bottom-right-radius: 1rem;
            }
            .hero h1{
                font-size:3rem;
                font-weight:bolder;
            }
            .hero h3{
                font-size:2rem;
                font-weight:bold;
            }
            .hero p{
                font-size:1.4rem;
                font-weight:light;
            }
        </style>
        <div class="hero editable">
            <h1 class="field">Title</h1>
            <h3 class="field">Subtitle</h3>
            <p class="field">content</p>
        </div>
        `
        initializeComponent(shadow)
    }
}

customElements.define('hero-cta', Hero);