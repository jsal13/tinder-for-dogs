<template>
  <div id="app">
    <Home />
    <h1>{{ apiAddress }}</h1>
    <p>hi</p>
  </div>
</template>

<script>
import axios from "axios";
import Home from "./components/Home.vue";

export default {
  name: "app",
  data() {
    return {
      apiAddress: process.env.VUE_APP_API_ADDRESS
    };
  },
  components: {
    Home
  },
  mounted() {
    axios({
      method: "get",
      url: `${this.apiAddress}/dog`,
      params: { dog_type: "American_Husky" }
    }).then(response => {
      console.log(response.data); /* eslint-disable-line */
    });
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
