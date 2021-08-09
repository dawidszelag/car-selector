<template>
  <div class="question">
    <h2>Who will be your passenger(s)? Select all that apply</h2>
    <div class="answers-box">
    <label class="option">
      <input
          type="checkbox"
          v-model="noPassengers"

      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>no passengers - I drive solo</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="bigFamily"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>big family</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="moreThanOneAdultOccasionally"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>more than 1 adult - occasionally</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="moreThanOneAdultRegularly"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>more than 1 adult - regularly</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="smallChildren"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>small children</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="elderlyUsingFrontSeat"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>elderly using front seat</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="elderlyUsingBackSeat"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>elderly using back seat</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="largeDog"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>large dog(s)</span>
    </label>

    <label class="option">
      <input
          type="checkbox"
          v-model="unsureFlexibility"
      />
      <font-awesome-icon
          icon="check-square"
      />
      <span>unsure - I want flexibility</span>
    </label>
  </div>
  </div>
</template>

<script>
export default {
  name: "Question7",
  data() {
    return {
      unsure: false,
    }
  },
  computed: {
    noPassengers: {
      get() {
        return this.$store.state.query.solo_drive;
      },
      set(value) {
        this.$store.state.query.solo_drive = value;
      }

    },
    bigFamily: {
      get() {
        return this.$store.state.query.big_family;
      },
      set(value) {
        this.$store.state.query.big_family = value;
      }
    },
    moreThanOneAdultOccasionally: {
      get() {
        return this.$store.state.query.occasionally_plus_one_adult;
      },
      set(value) {
        this.$store.state.query.occasionally_plus_one_adult = value;
      }
    },
    moreThanOneAdultRegularly: {
      get() {
        return this.$store.state.query.regularly_plus_one_adult;
      },
      set(value) {
        this.$store.state.query.regularly_plus_one_adult = value;
      }
    },
    smallChildren: {
      get() {
        return this.$store.state.query.children;
      },
      set(value) {
        this.$store.state.query.children = value;
      }
    },
    elderlyUsingFrontSeat: {
      get() {
        return this.$store.state.query.elderly_front_seat;
      },
      set(value) {
        this.$store.state.query.elderly_front_seat = value;
      }
    },
    elderlyUsingBackSeat: {
      get() {
        return this.$store.state.query.elderly_back_seat;
      },
      set(value) {
        this.$store.state.query.elderly_back_seat = value;
      }
    },
    largeDog: {
      get() {
        return this.$store.state.query.dogs;
      },
      set(value) {
        this.$store.state.query.dogs = value;
      }
    },
    unsureFlexibility: {
      get() {
        return this.$store.state.query.flexible;
      },
      set(value) {
        this.$store.state.query.flexible = value;
      }
    },
  },


}
</script>

<style scoped>

</style>