<template>
  <div class="car_gallery" v-if="images.length">
    <div class="section-text-d">
      LET'S LOOK AT IT
      <div class="section-text-subtitle">GALLERY</div>
    </div>
    <div class="gallery">
      <div class="image-list">
        <div v-for="image in images" :key="image.id" class="gallery_item">
          <img :src="OpenAPI.BASE + image.image" @click="showImage(images.indexOf(image))" alt="">
        </div>
      </div>
      <div class="main-image">
        <img :src="OpenAPI.BASE + currentImage.image" alt="">
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">

import {OpenAPI} from '../api';
import {defineProps, ref} from "vue";
const props = defineProps(['images'])
const currentImage = ref(props.images[0])
const showImage = (imageIdx) => {
  currentImage.value = props.images[imageIdx]
}
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
  padding: 0 5px;
  max-height: 400px;
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
}
.gallery {
  display: flex;
  justify-content: space-between;
}
</style>