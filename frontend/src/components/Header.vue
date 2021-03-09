<template>
  <v-app-bar app color="cyan">
    <v-row justify="center" align="center">
      <h1 class="text-h2 browndarken4--text user-select-none">
        Mapping Transcription Factor Binding Sites
      </h1>
    </v-row>
  </v-app-bar>
</template>

<script>
export default {
  methods: {
    toggleView() {
      this.$emit("switch");
    },
  },
};
</script>

<style lang="scss">
#switch-view-button {
  position: absolute;
  right: 5px;
}
.user-select-none {
  user-select: none;
}
</style>