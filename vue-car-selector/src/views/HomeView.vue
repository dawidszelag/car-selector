<template>
  <div class="container" :style="{ backgroundImage: 'url(' + bgImage + ')' }"
       style="background-position: center;
              background-size: cover;">
    <div class="logo">
      <img :src="Logo">
    </div>
    <div class="content">
      <InfoBox class="box"/>
      <Questions class="box" @ready="handlerFormReady" v-if="!appStore.showResults"/>
      <SearchResults class="box" v-else/>
    </div>
    <div class="footer">
      <div class="nav-button" @click="appStore.showResults=false" v-if="appStore.showResults">
        BACK TO QUESTIONS
      </div>
    </div>
  </div>

</template>

<script setup lang="ts">
import Logo from "@/assets/logo.png"
import bgImage from "@/assets/bg-pc.jpg"
import InfoBox from "../components/InfoBox";
import Questions from "../components/Questions";
import SearchResults from "../components/SearchResults";
import {useAppStore} from "../store";

const appStore = useAppStore();
const handlerFormReady = (_form: {}) => {
  appStore.setForm(_form);
  appStore.resetFeedback();
  appStore.showResults = true;
}
</script>

<style scoped lang="less">
.container .content {
  display: flex;
  flex-wrap: nowrap;
  width: 100%;
  .box {
    width: 50%;
    display: flex;
    flex-direction: column;
    overflow-x: hidden;
    padding: 100px 10%;
    height: 100vh;
  }
}

.container .footer{
  position: absolute;
  padding-left: 5%;
}

</style>