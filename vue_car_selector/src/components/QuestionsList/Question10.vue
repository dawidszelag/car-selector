<template>
  <div class="question">
    <h2>How many doors do you need?</h2>
    <div class="answers-box">
    <label class="option">
      <input
          type="radio"
          v-model="doors"
          value="1"

      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>2 doors</span>
    </label>

    <label class="option">
      <input
          type="radio"
          v-model="doors"
          value="2"
      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>4 doors</span>
    </label>

    <label class="option">
      <input
          type="radio"
          v-model="doors"
          value="3"
      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>unsure - we will consider all suitable options based on your passengers</span>
    </label>
    <label class="option">
      <input
          type="radio"
          v-model="doors"
          value="4"
      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>doesn’t matter - we will consider both options</span>
    </label>
  </div>
  </div>
</template>

<script>
export default {
  name: "Question10",
  watch: {
    doors() {
      this.$store.state.query.doors_2 = false;
      this.$store.state.query.doors_4 = false;
      this.$store.state.query.doors_unsure = false;
      this.$store.state.query.doors_dosnt_matter = false;
      switch (parseInt(this.doors)) {
        case 1:
          this.$store.state.query.doors_2 = true;
          break;
        case 2:
          this.$store.state.query.doors_4 = true;
          break;
        case 3:
          this.$store.state.query.doors_unsure = true;
          break;
        case 4:
          this.$store.state.query.doors_dosnt_matter = true;
          break;
      }
    }
  },
  computed: {
    doors: {
      get() {
        return this.$store.state.question_10;
      }
      ,
      set(value) {
        this.$store.state.question_10 = value;
      }

    }
  }

}
</script>

<style scoped>

</style>