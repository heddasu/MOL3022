<template>
  <v-app>
    <Header />
    <v-main>
      <Input/>
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import Header from "./components/Header";
import Footer from "./components/Footer";
import Input from "./views/Input";

export default {
  components: {
    Header,
    Input,
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