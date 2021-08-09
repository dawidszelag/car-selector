<template>
  <div class="question">
    <h2 style="margin-bottom: 0">Which features are important to you?</h2>
    <h5 style="margin: 0 0 20px 0">Select at least 2, max X TBC so that we can better match the right car for you</h5>
    <div class="answers-box">


      <label class="option">
        <input
            type="checkbox"
            v-model="cabin"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>premium cabin</span>
      </label>
      <label class="option">
        <input
            type="checkbox"
            v-model="comfort"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>comfort</span>
      </label>


      <label class="option">
        <input
            type="checkbox"
            v-model="infoSystem"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>high-tech infotainment system</span>
      </label>
      <label class="option">
        <input
            type="checkbox"
            v-model="style"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>overall style</span>
      </label>

      <br>

      <label class="option">
        <input
            type="checkbox"
            v-model="practicality"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>practicality - interior & space</span>
      </label>

      <label class="option">
        <input
            type="checkbox"
            v-model="foldingRearSeats"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>folding rear seats</span>
      </label>
      <label class="option">
        <input
            type="checkbox"
            v-model="adultsProtection"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>safety - adults protection</span>
      </label>

      <label class="option">
        <input
            type="checkbox"
            v-model="childrenProtection"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>safety - children protection</span>
      </label>
      <label class="option">
        <input
            type="checkbox"
            v-model="roadUserProtection"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>safety - road user protection</span>
      </label>
      <label class="option">
        <input
            type="checkbox"
            v-model="assistanceSystems"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>safety - assistance systems</span>
      </label>
      <label class="option">
        <input
            type="checkbox"
            v-model="warrantyOver5Years"

        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>warranty minimum 5 years (please note we will only consider the following brands - Toyota, Kia, Mercedes-Benz, Hyundai TBC)</span>
      </label>

    </div>
  </div>
</template>

<script>
export default {
  name: "Question15",
  data() {
    return {
      default_value: 6,
      default_value_2: 60,
    }
  },
  computed: {
    adultsProtection: {
      get() {
        return this.$store.state.query.safety_adult;
      },
      set(value) {
        this.$store.state.query.safety_adult = value;
      }
    },
    childrenProtection: {
      get() {
        return this.$store.state.query.safety_child;
      },
      set(value) {
        this.$store.state.query.safety_child = value;
      }
    },
    roadUserProtection: {
      get() {
        return this.$store.state.query.safety_road_user;
      },
      set(value) {
        this.$store.state.query.safety_road_user = value;
      }
    },
    assistanceSystems: {
      get() {
        return this.$store.state.query.safety_systems;
      },
      set(value) {
        this.$store.state.query.safety_systems = value;
      }
    },


    warrantyOver5Years: {
      get() {
        return this.$store.state.query.warranty_over_5_years;
      },
      set(value) {
        this.$store.state.query.warranty_over_5_years = value;
      }
    },


    comfort: {
      get() {
        return this.$store.state.query.comfort;
      },
      set(value) {
        this.$store.state.query.comfort = value;
      }
    },

    practicality: {
      get() {
        return this.$store.state.query.practicality;
      },
      set(value) {
        this.$store.state.query.practicality = value;
      }
    },

    cabin: {
      get() {
        return this.$store.state.query.cabin;
      },
      set(value) {
        this.$store.state.query.cabin = value;
      }
    },

    style: {
      get() {
        return this.$store.state.query.style;
      },
      set(value) {
        this.$store.state.query.style = value;
      }
    },

    foldingRearSeats: {
      get() {
        return this.$store.state.query.folding_rear_seats;
      },
      set(value) {
        this.$store.state.query.folding_rear_seats = value;
      }
    },
    infoSystem: {
      get() {
        return this.$store.state.query.info_system;
      },
      set(value) {
        this.$store.state.query.info_system = value;
      }
    },

  },


}
</script>

<style scoped>

</style>