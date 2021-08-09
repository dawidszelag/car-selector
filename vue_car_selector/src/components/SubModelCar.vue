<template>
  <div>
    <div class="models_results">
      <div class="model_view">
        <div class="model_img">
          <span class="price">${{ formatPrice(carInfo.markets[0].price) }}</span>
          <div v-if="carInfo.images[0]" class="img" v-bind:style="modelImg"> </div>
          <div v-else class="img" style="background: url('https://via.placeholder.com/800x500') no-repeat center;"> </div>
          <div class="model_name">{{ carInfo.name }}</div>
        </div>
        <button @click="viewCar" class="btn_view">DETAILS</button>
        <div class="sub_model_info">
          <ul>

            <li>
              <div class="name">FULL NAME</div>
              <div class="value">{{ carInfo.name }}</div>
            </li>
            <li>
              <div class="name">BRAND</div>
              <div class="value">{{ carInfo.model.brand.name }}</div>
            </li>
            <li>
              <div class="name">MODEL</div>
              <div class="value">{{ carInfo.model.name }}</div>
            </li>
            <li>
              <div class="name">ENGINE SIZE</div>
              <div class="value">{{ carInfo.engine_size }} cm3</div>
            </li>
            <li>
              <div class="name">POWER kW</div>
              <div class="value">{{ carInfo.power_kw }}</div>
            </li>
            <li>
              <div class="name">TRANSMISSION</div>
              <div class="value">{{ carInfo.transmission }}</div>
            </li>
            <li>
              <div class="name">FUEL TYPE</div>
              <div class="value">{{ carInfo.fuel_type }}</div>
            </li>
            <li>
              <div class="name">BODY</div>
              <div class="value">{{ carInfo.body }}</div>
            </li>
            <li>
              <div class="name">PRICE</div>
              <div class="value">${{ formatPrice(carInfo.markets[0].price) }}</div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SubModelCar",
  props: ['carInfo',],
  data() {
    return {
      baseUrl: this.$store.state.base_media_url,
    }
  },
  methods: {
    viewCar() {
      this.$router.push({name: 'car', params: {carId: this.carInfo.id}})
    },
    formatPrice(value) {
      let val = (value / 1).toFixed(0).replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    }
  },
  computed: {
    modelImg: function () {
      return {
        background: `url(${this.carInfo.images[0].image}) no-repeat center`,
      }
    }
  }
}
</script>

<style scoped>

.models_results {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
}

.model_view .img {
  width: 100%;
  min-height: 180px;
  margin-bottom: 5px;
  background-size: cover;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}
.model_view {
  min-width: 100%;
}


.model_view .model_img {
  position: relative;
}

.model_view .model_img .model_name {
  position: absolute;
  bottom: 10px;
  left: 10px;
  font-weight: 700;
}

.model_view .btn_view {
  width: 100%;
  height: 40px;
  background: #ff005a;
  border: none;
  color: white;
  opacity: 0.8;
  font-weight: 600;
}

.model_view .btn_view:hover {
  opacity: 1;
  cursor: pointer;
}

.price {
  position: absolute;
  right: 10px;
  font-weight: 700;
  font-size: 21px;
  top: 5px;
}

.sub_model_info ul {
  list-style: none;
  padding-left: 0;
}

.sub_model_info ul li {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  padding-bottom: 8px;

}

.sub_model_info ul li .value {
  font-weight: 700;
  text-align: right;
  font-size: 13px;
}
</style>