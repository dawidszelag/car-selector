<template>
  <div class="question">
    <h2>What engine size would you like?</h2>
    <div class="answers-box">
    <label class="option">
      <input
          type="radio"
          v-model="engine"
          value="1"

      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>up to 1.0 L</span>
    </label>

    <label class="option">
      <input
          type="radio"
          v-model="engine"
          value="2"
      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>1.0-2.0 L</span>
    </label>

    <label class="option">
      <input
          type="radio"
          v-model="engine"
          value="3"
      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>2.0-3.0 L</span>
    </label>
    <label class="option">
      <input
          type="radio"
          v-model="engine"
          value="4"
      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>bigger than 3.0 L</span>
    </label>
    <label class="option">
      <input
          type="radio"
          v-model="engine"
          value="5"
      />
      <font-awesome-icon
          icon="check-circle"
      />
      <span>unsure</span>
    </label>
  </div>
  </div>
</template>

<script>
export default {
  name: "Question14",
  watch: {
    engine() {
      this.$store.state.query.engine_up_to_1 = false;
      this.$store.state.query.engine_1_2 = false;
      this.$store.state.query.engine_2_3 = false;
      this.$store.state.query.engine_bigger_then_3 = false;
      this.$store.state.query.engine_unsure = false;
      switch (parseInt(this.engine)) {
        case 1:
          console.log('ture')
          this.$store.state.query.engine_up_to_1 = true;
          break;
        case 2:
          this.$store.state.query.engine_1_2 = true;
          break;
        case 3:
          this.$store.state.query.engine_2_3 = true;
          break;
        case 4:
          this.$store.state.query.engine_bigger_then_3 = true;
          break;
        case 5:
          this.$store.state.query.engine_unsure = true;
          break;
      }
    }
  },
  computed: {
    engine: {
      get() {
        return this.$store.state.question_14;
      }
      ,
      set(value) {
        this.$store.state.question_14 = value;
      }

    }
  }

}
</script>

<style scoped>

</style>