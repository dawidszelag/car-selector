<template>
  <div class="question">
    <h2>Where will you drive?</h2>
    <div class="answers-box">
    <label class="option">
      <input
          type="radio"
          v-model="whereDrive"
          value="1"
      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>mainly local</span>
    </label>

    <label class="option">
      <input
          type="radio"
          v-model="whereDrive"
          value="2"
      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>mainly distance</span>
    </label>

    <label class="option">
      <input
          type="radio"
          v-model="whereDrive"
          value="3"
      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>mixed</span>
    </label>
  </div>
  </div>
</template>

<script>
export default {
  name: "Question3",
  watch: {
    whereDrive() {
      this.$store.state.query.short_distance = false;
      this.$store.state.query.long_distance = false;
      this.$store.state.query.mixed_distance = false;
      switch (parseInt(this.whereDrive)) {
        case 1:
          this.$store.state.query.short_distance = true;
          break;
        case 2:
          this.$store.state.query.long_distance = true;
          break;
        case 3:
          this.$store.state.query.mixed_distance = true;
          break;
      }
    }
  },
  computed: {
    whereDrive: {
      get() {
        return this.$store.state.question_3;
      },
      set(value) {
        this.$store.state.question_3 = value;
      }

    },
  },

}
</script>

<style scoped>

</style>