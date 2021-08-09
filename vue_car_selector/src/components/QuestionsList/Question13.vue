<template>
  <div class="question">
    <h2>What transmission would you like?</h2>
    <div class="answers-box">
    <label class="option">
      <input
          type="radio"
          v-model="transmission"
          value="1"

      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>automatic</span>
    </label>

    <label class="option">
      <input
          type="radio"
          v-model="transmission"
          value="2"
      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>manual</span>
    </label>

    <label class="option">
      <input
          type="radio"
          v-model="transmission"
          value="3"
      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>doesn’t matter</span>
    </label>
  </div>
  </div>
</template>

<script>
export default {
  name: "Question13",
  watch: {
    transmission() {
      this.$store.state.query.transmission_automatic = false;
      this.$store.state.query.transmission_manual = false;
      this.$store.state.query.transmission_dosnt_matter = false;
      switch (parseInt(this.transmission)) {
        case 1:
          this.$store.state.query.transmission_automatic = true;
          break;
        case 2:
          this.$store.state.query.transmission_manual = true;
          break;
        case 3:
          this.$store.state.query.transmission_dosnt_matter = true;
          break;
      }
    }
  },
  computed: {
    transmission: {
      get() {
        return this.$store.state.question_13;
      }
      ,
      set(value) {
        this.$store.state.question_13 = value;
      }

    }
  }

}
</script>

<style scoped>

</style>