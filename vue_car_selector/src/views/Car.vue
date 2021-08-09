<template>
  <div class="content">
    <div class="box">
      <div class="box-title">
        CAR DETAILS
      </div>
      <div v-if="isDataLoading" class="center-content">
        <div class="lds-hourglass"></div>
      </div>
      <div v-else-if="car">
        <h2>{{ car.name }}</h2>
        <div class="box-content">
          <div class="car_details">

            <div class="car_info">
              <div class="car_main_img">
                <img v-if="car.images[mainImageIndex]" :src="car.images[mainImageIndex].image" alt="">
                <img v-else src="https://via.placeholder.com/350x250" alt="">
              </div>
              <div class="cat_details_bar">VEHICLE SUMMARY</div>
              <div class="sub_model_info">
                <ul>
                  <li>
                    <div class="name">BRAND</div>
                    <div class="value">{{ car.model.brand.name }}</div>
                  </li>
                  <li>
                    <div class="name">MODEL</div>
                    <div class="value">{{ car.model.name }}</div>
                  </li>
                  <li>
                    <div class="name">PRICE</div>
                    <div class="value">${{ formatPrice(car.markets[0].price) }}</div>
                  </li>
                </ul>
                <ul>
                  <li>
                    <div class="name">BODY</div>
                    <div class="value">{{ car.body }}</div>
                  </li>
                  <li>
                    <div class="name">DOORS</div>
                    <div class="value">{{ car.doors }}</div>
                  </li>
                  <li>
                    <div class="name">SEATS</div>
                    <div class="value">{{ car.seats }}</div>
                  </li>


                </ul>
                <ul>
                  <li>
                    <div class="name">LENGTH</div>
                    <div class="value">{{ car.length }}</div>
                  </li>
                  <li>
                    <div class="name">WIDTH</div>
                    <div class="value">{{ car.width }}</div>
                  </li>
                  <li>
                    <div class="name">HEIGHT</div>
                    <div class="value">{{ car.height }}</div>
                  </li>
                  <li>
                    <div class="name">WHEEL BASE</div>
                    <div class="value">{{ car.wheelbase }}</div>
                  </li>
                  <li>
                    <div class="name">TARE MASS (KG)</div>
                    <div class="value">{{ car.tare_mass }}</div>
                  </li>
                  <li>
                    <div class="name">GROUND CLEARANCE</div>
                    <div class="value">{{ car.ground_clearance }}</div>
                  </li>
                </ul>
                <ul>
                  <li>
                    <div class="name">MINIMUM BOOT SPACE</div>
                    <div class="value">{{ car.min_boot_space }}</div>
                  </li>
                  <li>
                    <div class="name">MAXIMUM BOOT SPACE</div>
                    <div class="value">{{ car.max_boot_space }}</div>
                  </li>
                  <li>
                    <div class="name">FOLDABLE BACK SEATS - YES/NO</div>
                    <div class="value"><span v-if=" car.foldable_seats">YES</span><span v-else>NO</span></div>
                  </li>

                </ul>
                <ul>
                  <li>
                    <div class="name">TRANSMISSION</div>
                    <div class="value">{{ car.transmission }}</div>
                  </li>
                  <li>
                    <div class="name">GEARS</div>
                    <div class="value">{{ car.gears }}</div>
                  </li>
                  <li>
                    <div class="name">DRIVE</div>
                    <div class="value">{{ car.drive }}</div>
                  </li>

                </ul>
                <ul>
                  <li>
                    <div class="name">ENGINE LOCATION</div>
                    <div class="value">{{ car.engine_location }}</div>
                  </li>
                  <li>
                    <div class="name">ENGINE SIZE</div>
                    <div class="value">{{ car.engine_size }}cm3</div>
                  </li>
                  <li>
                    <div class="name">ENGINE CONFIGURATION</div>
                    <div class="value">{{ car.engine_configuration }}</div>
                  </li>
                  <li>
                    <div class="name">CYLINDERS</div>
                    <div class="value">{{ car.cylinders }}</div>
                  </li>
                  <li>
                    <div class="name">POWER HP</div>
                    <div class="value">{{ car.power_kw }}</div>
                  </li>
                  <li>
                    <div class="name">POWER kW</div>
                    <div class="value">{{ car.power_hp }}</div>
                  </li>
                  <li>
                    <div class="name">POWER rpm</div>
                    <div class="value">{{ car.power_rpm }}</div>
                  </li>
                  <li>
                    <div class="name">TORQUE</div>
                    <div class="value">{{ car.torque_nm }}</div>
                  </li>
                  <li>
                    <div class="name">TORQUE RPM</div>
                    <div class="value">{{ car.torque_rpm }}</div>
                  </li>
                  <li>
                    <div class="name">ACCELERATION 0-100 (SEC)</div>
                    <div class="value">{{ car.acceleration }}</div>
                  </li>
                  <li>
                    <div class="name">TOP SPEED (KM/H)</div>
                    <div class="value">{{ car.top_speed }}</div>
                  </li>

                </ul>
                <ul>
                  <li>
                    <div class="name">FUEL TYPE</div>
                    <div class="value">{{ car.fuel_type }}</div>
                  </li>
                  <li>
                    <div class="name">FUEL CAPACITY</div>
                    <div class="value">{{ car.fuel_capacity }}</div>
                  </li>
                  <li>
                    <div class="name">FUEL COMBINED</div>
                    <div class="value">{{ car.fuel_combined }}</div>
                  </li>
                  <li>
                    <div class="name">FUEL URBAN</div>
                    <div class="value">{{ car.fuel_urban }}</div>
                  </li>
                  <li>
                    <div class="name">FUEL AVERAGE DISTANCE (KM)</div>
                    <div class="value">{{ car.fuel_average_distance }}</div>
                  </li>
                  <li v-if="car.electric_range">
                    <div class="name">ELECTRIC RANGE (KM)</div>
                    <div class="value">{{ car.electric_range }}</div>
                  </li>

                </ul>
                <ul>
                  <li>
                    <div class="name">ANCAP RATING - OUT OF 5*</div>
                    <div class="value">{{ car.ancap }}</div>
                  </li>
                  <li>
                    <div class="name">WARRANTY (YEARS)</div>
                    <div class="value">{{ car.warranty_years }}</div>
                  </li>
                  <li>
                    <div class="name">WARRANTY (KM)</div>
                    <div class="value">{{ car.warranty_distance }}</div>
                  </li>
                  <li v-if="parseInt(car.battery_warranty_years)">
                    <div class="name">BATTERY WARRANTY (YEARS)</div>
                    <div class="value">{{ car.battery_warranty_years }}</div>
                  </li>
                </ul>
              </div>
            </div>

            <div class="car_gallery">
              <div class="cat_details_bar">
                GALLERY
              </div>
              <div v-for="image in car.images" :key="image.pk" class="gallery_item">
                <img :src="image.image" @click="showImage(car.images.indexOf(image))" alt="">
              </div>
              <div v-if="!car.images.length" class="gallery_item">
                <img src="https://via.placeholder.com/350x250" alt="">
              </div>


            </div>
          </div>
        </div>
        <div class="navigation">

          <button
              class="button-back"
              @click="backToSubModels"
          >
            Back
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Car",
  components: {},
  data() {
    return {
      carId: this.$route.params.carId,
      car: false,
      mainImageIndex: 0,
      isDataLoading: false,
    }
  },
  methods: {
    showImage(id) {
      this.mainImageIndex = id;
    },
    backToSubModels() {
      this.$router.push({name: 'sub-models', params: {modelId: this.car.model.id}})
    },
    formatPrice(value) {
      let val = (value / 1).toFixed(0).replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
    }
  },
  created() {
    this.isDataLoading = true;
    axios.get(`car/${this.carId}`).then(({data}) => {
      this.car = data
      this.isDataLoading = false;
    }).catch(error => {
      this.isDataLoading = false
      console.log(error)
    })
  }
}
</script>

<style scoped>
.content {
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: flex-start ;
  justify-content: center;
  padding-top: 200px;
  padding-bottom: 100px;
  min-height: 100vh;
  flex: 1;
}

.box {
  width: 80%;
  max-width: 650px;
}

.box-content {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.box-title {
  color: #ff005a;
  font-weight: 600;
  margin-bottom: 10px;
}

.car_details {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.car_gallery img,
.car_main_img img {
  width: 100%;
  height: auto;

}

.car_gallery img {
  cursor: pointer;
}

.car_info {
  flex-basis: 70%;
}

.car_gallery {
  flex-basis: 28%;
}

.cat_details_bar {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 40px;
  background: #ff005a;
  border: none;
  color: white;
  opacity: 0.8;
  font-weight: 600;
  margin-bottom: 10px;
}

.car_info ul {
  list-style: none;
  padding-left: 0;
}

.car_info ul li {
  display: flex;
  justify-content: space-between;
  font-size: 15px;
  padding-bottom: 7px;
}

.car_info ul li .value {
  font-weight: 700;
  text-align: right;
}

.navigation {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 20px;
}

.navigation button {
  padding: 8px 15px;
  font-size: 12px;
}

.navigation span {
  font-size: 13px;
  font-weight: 700;
}

</style>