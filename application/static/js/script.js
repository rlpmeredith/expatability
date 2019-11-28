//console.log("Hello from app.js!")

const app = new Vue({
      el: '#app',
      vuetify: new Vuetify(),
      data: {
            message: 'Hello, my name is Rob!'
      },
      methods: {
            clicked: function() {
                console.log('test clicked')
            }
      },
})
