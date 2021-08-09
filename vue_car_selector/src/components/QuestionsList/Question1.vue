<template>
  <div class="question">
    <h2>Gender(s) of the driver(s) - select all that apply</h2>
    <div class="answers-box">
    <label class="option">
      <input
          type="checkbox"
          v-model="setCatForWoman"

      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>female</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="setCarForMan"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>male</span>
    </label>
    <label class="option">
      <input
          type="checkbox"
          v-model="prefer_not_to_say"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>prefer not to say</span>
    </label>
  </div>
  </div>
</template>

<script>
export default {
  name: "Question1",
  data() {
    return {
      prefer_not_to_say: false,
    }
  },
  computed: {
    setCatForWoman: {
      get() {
        return this.$store.state.query.car_for_woman;
      },
      set(value) {
        if (value) {
          this.prefer_not_to_say = false;
        }
        this.$store.state.query.car_for_woman = value;
      }

    },
    setCarForMan: {
      get() {
        return this.$store.state.query.car_for_man;
      },
      set(value) {
        if (value) {
          this.prefer_not_to_say = false;
        }
        this.$store.state.query.car_for_man = value;
      }
    },
  },
  watch: {
    prefer_not_to_say() {
      if (this.prefer_not_to_say) {
        this.setCatForWoman = false;
        this.setCarForMan = false;
      }
    }
  }

}
</script>

<style scoped>

</style>