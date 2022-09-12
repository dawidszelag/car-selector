<template>
  <div class="container" :style="{ backgroundImage: 'url(' + bgImage + ')' }"
       style="background-position: center;
  background-size: cover;">
    <div class="logo">
      <img :src="Logo">
    </div>
    <info-box class="box"/>
    <questions class="box" @ready="handlerFormReady" v-if="!appStore.showResults"/>
    <search-results class="box" :form="form" v-else/>
    <div class="nav-right" @click="appStore.showResults=false" v-if="appStore.showResults">
      BACK TO FORM
    </div>
  </div>
</template>

<script setup>
import Logo from "@/assets/logo.png"
import bgImage from "@/assets/bg-pc.jpg"
import InfoBox from "../components/InfoBox";
import Questions from "../components/Questions";
import SearchResults from "../components/SearchResults";
import {useAppStore} from "../store";

const appStore = useAppStore();
const handlerFormReady = (_form) => {
  appStore.setForm(_form);
  appStore.showResults = true;
}
</script>

<style scoped lang="less">
.container {
  display: flex;
  flex-wrap: nowrap;
  width: 100%;

  .box {
    width: 50%;
    display: flex;
    flex-direction: column;
    overflow-x: hidden;
    padding: 100px 10%;
  }
}
</style>