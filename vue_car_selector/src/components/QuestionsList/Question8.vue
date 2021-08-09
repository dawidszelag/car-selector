<template>
  <div class="question">
    <h2>Which fuel type would you like? Select all that apply</h2>
    <div class="answers-box">
      <label class="option" v-for="fuel_type in fuel_types" :key="fuel_type.name">
        <input
            type="checkbox"
            :checked="fuelTypesList.includes(fuel_type.name)"
            @change="addFuelTypeToList(fuel_type.name)"
        />
        <font-awesome-icon
            icon="check-square"
        />
        <span>{{ fuel_type.name }}</span>
      </label>
    </div>
  </div>
</template>

<script>

export default {
  name: "Question8",
  data() {
    return {
      fuel_types: [
        {
          name: 'Petrol',
        },
        {
          name: 'Diesel',
        },
        {
          name: 'Electric',
        },
        {
          name: 'Plug in Hybrid - Petrol',
        },
        {
          name: 'Plug in Hybrid - Diesel',
        },
        {
          name: 'Hybrid - Petrol',
        },
        {
          name: 'Hybrid - Diesel',
        }
      ],
    }
  },
  methods: {
    addFuelTypeToList(fuel_type) {
      this.$store.state.query.fuel_type_list.push(fuel_type)
    }
  },
  computed: {
    fuelTypesList: function () {
      console.log(this.$store.state.query.fuel_type_list)
      return this.$store.state.query.fuel_type_list;
    }
  },
}
</script>

<style scoped>
input {
  width: 70%;
  cursor: pointer;
}

.budget-info {
  width: 30%;
  text-align: right;
}
</style>