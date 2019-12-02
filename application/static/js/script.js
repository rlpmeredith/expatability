
const app = new Vue({
       el: '#app',
       vuetify: new Vuetify(),
       data() {
            return {
            headers: [
                {
                  text: 'Cityname',
                  align: 'center',
                  sortable: 'false',
                  value: "cityname"
                  },
                { text: "Index", value: "index" }
                ],
//            citylist: [{"cityname": false, "index": false}],
            citylist: [],
            cards: [
                { title: 'Does the amount of sunlight in a day matter to you?', src: './static/images/Valletta.jpg', flex: 4, sortorder: 'daylength' },
                { title: 'Do you want to see if a place ranks high in acceptance of immigrants?', src: './static/images/paris.jpg', flex: 4, sortorder: 'migrants' },
                { title: 'How about looking at cities ranked by cost of living?', src: './static/images/London.jpg', flex: 4, sortorder: 'cost' },
                { title: "Do you want to narrow your search based on a city's average temperature?", src: './static/images/Stockholm.jpg', flex: 4, sortorder: 'weather' },
                { title: "Does a location's overall happiness matter to you?", src: './static/images/happiness.jpg', flex: 4, sortorder: 'happiness' },
                { title: 'Or would you like to search for a particular city?', src: './static/images/sign.jpg', flex: 4 },
            ]}
       },
       methods: {
            get_data(sortorder) {
                const self = this;
                const url = `api/citylist?order=${sortorder}`
                fetch(url).then(res => res.json())
                .then(json => self.citylist = json['citylist'])
                }
      }
})
