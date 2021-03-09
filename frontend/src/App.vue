<template>
  <v-app>
    <Header @switch="changeView" />
    <v-main>
      <Input v-if="showInput" ref="input" />
      <Result v-else />
    </v-main>
    <Footer @switch="changeView" />
  </v-app>
</template>

<script>
import Header from "./components/Header";
import Footer from "./components/Footer";
import Input from "./views/Input";
import Result from "./views/Result";

export default {
  components: {
    Header,
    Input,
    Result,
    Footer,
  },
  data: () => ({
    showInput: true,
  }),
  methods: {
    changeView() {
      this.showInput = !this.showInput;
    },
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