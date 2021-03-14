<template>
  <v-app>
    <Header />
    <v-main>
      <Body/>
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import Header from "./components/Header";
import Footer from "./components/Footer";
import Body from "./views/Body";

export default {
  components: {
    Header,
    Body,
    Footer,
  },
  data: () => ({
  }),
  methods: {
  },
};
</script>

<style lang="scss">
@media (min-width: 1904px) {
  .container {
    max-width: 1185px !important;
  }
}
</style>