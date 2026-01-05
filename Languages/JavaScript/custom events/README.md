Custom events are a way in javascript to dispatch events that you can setup listeners for. Similar to events like `onclick` for a button, you can emit a custom event, and then have dedicated listeners for it.

To construct an error use:

```js
const typename = ""// Some string, (will be what you bind the listener to)
const options = {
    detail:{
        // Values you want to pass to the listener go here
    }
}

new CustomEvent(typename, options)
```

So a full example would be something like:

```js
const typename = "MyEvent"
const options = {
    detail:{
        name:"kieran"
    }
}
const callback = (event) => {console.log(event.detail)} // A function to do something
const target = document // Something to target, can be the document or any HTMLElement


const myCustomEvent = new CustomEvent(typename, options)

target.addEventListener(typename, callback) // To listen to the event

target.dispatchEvent(myCustomEvent) // To actually emit the event
```

## References

- [CustomEvent: CustomEvent() constructor - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent/CustomEvent)
- [An Essential Guide To JavaScript Custom Events](https://www.javascripttutorial.net/javascript-dom/javascript-custom-events/)
- [Custom events in JavaScript: A complete guide - LogRocket Blog](https://blog.logrocket.com/custom-events-in-javascript-a-complete-guide/)