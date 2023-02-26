<template>
  <div class="car_gallery">
    <div class="section-text-d">
      LET'S LOOK AT IT
      <div class="section-text-subtitle">GALLERY</div>
    </div>
    <div class="gallery">
      <div class="image-list">
        <div v-for="image in images" :key="image.id" class="gallery_item">
          <img :src="OpenAPI.BASE + image.image" @click="currentImageIndex = images.indexOf(image)" alt="">
        </div>
      </div>
      <div class="main-image"
        :style="{ backgroundImage: 'url(' +  OpenAPI.BASE + currentCarImage?.image  + ')' }"
        style="background-position: center; background-size: cover;">
      </div>
    </div>
  </div>
  <slot/>
</template>

<script setup lang="ts">

import {OpenAPI} from '../api';
import {computed, defineProps, ref} from "vue";
const props = defineProps(['images'])
const currentImageIndex = ref(0)


const currentCarImage = computed(() => {
  return props.images?.length ? props.images[currentImageIndex.value] : undefined
})
</script>
<style lang="less" scoped>

.main-image img {
  width: 100%;
  height: auto;
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

.image-list{
  width: 25%;
  padding-right: 5px;
  height: 350px;
  overflow-y: scroll;
  .gallery_item img{
    width: 100%;
    height: auto;
  }
}
.gallery_item{
  width: 100%;
  height: auto;
}
.main-image{
  width: 73%;
  height: 350px;
}
.gallery {
  display: flex;
  justify-content: space-between;
}
</style>