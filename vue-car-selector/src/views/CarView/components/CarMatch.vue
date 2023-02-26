<template>
  <div>
    <div class="section-text-d" style="margin-top: 20px">
      WHAT'S SPECIAL?
      <div class="section-text-subtitle"> CARMATCH ASSESSMENTS</div>
    </div>
    <div class="carmatch">
      <div class="badge">
        <img v-if="car?.flexible && car.big_family" :src="FLEXIBILITY_AND_FAMILY_ACTIVE">
        <img v-else :src="FLEXIBILITY_AND_FAMILY_INACTIVE">
      </div>
      <div class="badge">
        <img v-if="car?.practicality > 8" :src="PRACTICALITY_ACTIVE">
        <img v-else :src="PRACTICALITY_INACTIVE">
      </div>
      <div class="badge">
        <img v-if="car?.comfort > 8" :src="COMFORT_ACTIVE">
        <img v-else :src="COMFORT_INACTIVE">
      </div>
      <div class="badge">
        <img v-if="(car?.safety_road_user + car.safety_child + car.safety_adult + car.safety_systems) > 250"
             :src="HIGHEST_SAFETY_RATING_ACTIVE">
        <img v-else :src="HIGHEST_SAFETY_RATING_INACTIVE">
      </div>
      <div class="badge">
        <img v-if="car?.min_boot_space > 250"
             :src="BIG_BOOT_ACTIVE">
        <img v-else :src="BIG_BOOT_INACTIVE">
      </div>
      <div class="badge">
        <img v-if="car?.info_system > 8"
             :src="HIGHTECH_INFOTAIMENT_ACTIVE">
        <img v-else :src="HIGHTECH_INFOTAIMENT_INACTIVE">
      </div>
      <div class="badge">
        <img v-if="car?.perfect_city_car" :src="PERFECT_FOR_CITY_ACTIVE">
        <img v-else :src="PERFECT_FOR_CITY_INACTIVE">
      </div>
      <div class="badge">
        <img v-if="car?.anna_for_women" :src="PERFECT_FOR_WOMAN_ACTIVE">
        <img v-else :src="PERFECT_FOR_WOMAN_INACTIVE">
      </div>
      <div class="badge">
        <img v-if="car?.sport_feel > 8"
             :src="SPORTSCAR_ACTIVE">
        <img v-else :src="SPORTSCAR_INACTIVE">
      </div>
      <div class="badge">
<!--        TODO-->
        <img v-if="false"
             :src="SPORTSCAR_ACTIVE">
        <img v-else :src="SPORTSCAR_INACTIVE">
      </div>
      <div class="badge">
        <img v-if="car?.heavy_off_road"
             :src="HEAVY_OFF_ROADER_ACTIVE">
        <img v-else :src="HEAVY_OFF_ROADER_INACTIVE">
      </div>
      <div class="badge">
        <img v-if="car?.max_charging_max_kw > 200"
             :src="RAPID_CHARGING_ACTIVE">
        <img v-else :src="RAPID_CHARGING_INACTIVE">
      </div>
      <div class="badge">
        <img v-if="car?.anna_cars" :src="ANNAS_CHOICE_ACTIVE">
        <img v-else :src="ANNAS_CHOICE_INACTIVE">
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import ANNAS_CHOICE_ACTIVE from "@/assets/badges/annas_choice_active.png"
import ANNAS_CHOICE_INACTIVE from "@/assets/badges/annas_choice_inactive.png"
import BIG_BOOT_ACTIVE from "@/assets/badges/big_boot_active.png"
import BIG_BOOT_INACTIVE from "@/assets/badges/big_boot_inactive.png"
import COMFORT_ACTIVE from "@/assets/badges/comfort_active.png"
import COMFORT_INACTIVE from "@/assets/badges/comfort_inactive.png"
import FLEXIBILITY_AND_FAMILY_ACTIVE from "@/assets/badges/flexibility_and_family_active.png"
import FLEXIBILITY_AND_FAMILY_INACTIVE from "@/assets/badges/flexibility_and_family_inactive.png"
import HEAVY_OFF_ROADER_ACTIVE from "@/assets/badges/heavy_off-roader_active.png"
import HEAVY_OFF_ROADER_INACTIVE from "@/assets/badges/heavy_off-roader_inactive.png"
import HIGHEST_SAFETY_RATING_ACTIVE from "@/assets/badges/highest_safety_rating_active.png"
import HIGHEST_SAFETY_RATING_INACTIVE from "@/assets/badges/highest_safety_rating_inactive.png"
import HIGHTECH_INFOTAIMENT_ACTIVE from "@/assets/badges/hightech_infotaiment_active.png"
import HIGHTECH_INFOTAIMENT_INACTIVE from "@/assets/badges/hightech_infotaiment_inactive.png"
import HOT_HATCH_ACTIVE from "@/assets/badges/hot_hatch_active.png"
import HOT_HATCH_INACTIVE from "@/assets/badges/hot_hatch_inactive.png"
import PERFECT_FOR_CITY_ACTIVE from "@/assets/badges/perfect_for_city_active.png"
import PERFECT_FOR_CITY_INACTIVE from "@/assets/badges/perfect_for_city_inactive.png"
import PERFECT_FOR_WOMAN_ACTIVE from "@/assets/badges/perfect_for_woman_active.png"
import PERFECT_FOR_WOMAN_INACTIVE from "@/assets/badges/perfect_for_woman_inactive.png"
import PRACTICALITY_ACTIVE from "@/assets/badges/practicality_active.png"
import PRACTICALITY_INACTIVE from "@/assets/badges/practicality_inactive.png"
import RAPID_CHARGING_ACTIVE from "@/assets/badges/rapid_charging_active.png"
import RAPID_CHARGING_INACTIVE from "@/assets/badges/rapid_charging_inactive.png"
import SPORTSCAR_ACTIVE from "@/assets/badges/sportscar_active.png"
import SPORTSCAR_INACTIVE from "@/assets/badges/sportscar_inactive.png"
import {defineProps, PropType} from "vue";
import type {CarDetailsOut} from "../../../api";

defineProps({
  car: {
    type: Object as PropType<CarDetailsOut>,
  }
});
</script>
<style scoped lang="less">
.carmatch {
  display: flex;
  flex-wrap: wrap;

  .badge {
    max-width: 18%;
    margin-right: 2%;
    margin-bottom: 1%;

    img {
      max-width: 100%;
      box-shadow: 0 2px 3px rgb(0 0 0 / 40%);
    }
  }
}

</style>