//console.log("Hello from app.js!")
//


//
//const app = new Vue({
//      el: '#app',
//      vuetify: new Vuetify(),
//      data: {
//            message: 'Success!'
//      },
//      methods: {
//            proceed() {
//                console.log('proceed')
//            }
//      },
//})



const Questions = new Vue({
       el: '#app',
       vuetify: new Vuetify(),
       data: {
            cards: [
                { title: 'Does the amount of sunlight in a day matter to you?', src: './static/images/Valletta.jpg', flex: 4, sortorder: 'daylength' },
                { title: 'Do you want to see if a place ranks high in acceptance of immigrants?', src: './static/images/paris.jpg', flex: 4 },
                { title: 'How about looking at cities ranked by cost of living?', src: './static/images/London.jpg', flex: 4 },
                { title: "Do you want to narrow your search based on a city's average temperature?", src: './static/images/Stockholm.jpg', flex: 4 },
                { title: "Does a location's overall happiness matter to you?", src: './static/images/happiness.jpg', flex: 4 },
                { title: 'Or would you like to search for a particular city?', src: './static/images/sign.jpg', flex: 4 },
            ],
      },
      methods: {
            proceed() {
                console.log('Hello')
            },
            get_data(sortorder) {
//                const url = `api/citylist?order=${sortorder}`
                console.log(${sortorder})
//                fetch(url, {
//                method: 'GET'
//                    }).then(res => res.json())
//                    .then((citydata) => this.happinessTable = citydata)
            }
      }
})




////const rankHappiness = (capital) => {
//const happinessRank = new Vue({
//    el: '#app',
//    vuetify: new Vuetify(),
//    data: {
//        happinessTable: {}
//    },
//    const url = `api/citylist`
//    fetch(url, {
//       method: 'GET'
//    }).then(res => res.json())
//        .then((data) => this.happinessTable = data)
//    }
//})



//const retrieveMessages = (chat_id, user_id) => {
//    // const data = {"chat_id": chat_id}
//    const url = `/api/chats/${chat_id}/messages?user_id=${user_id}`
//    fetch(url, {
//        method: 'GET'
//    }).then(res => res.json())
//        .then( data => addMessages(data))
//}



//const app = new Vue({
//    el: 'vue-app',
//    data: {
//        displayedBooks: {}
//    },
//    created() {
//        fetch('/library').then(response => response.json())
//            .then((data) => this.displayedBooks = data);
//    }
//});