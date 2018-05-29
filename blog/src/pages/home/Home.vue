<template>
    <div class="home">
        <nav class="navbar navbar-default">
            <div class="container-fluid">
                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">
                        <router-link to="/home/page/homepage" tag="li">首页</router-link>
                        <router-link to="webpage" tag="li">web</router-link>
                        <router-link to="pythonpage" tag="li">python</router-link>
                        <router-link to="jspage" tag="li">javascript</router-link>
                        <router-link to="htmlpage" tag="li">html</router-link>
                        <router-link to="csspage" tag="li">css</router-link>
                    </ul>
                </div><!-- /.navbar-collapse -->
            </div><!-- /.container-fluid -->
        </nav>
        <router-view></router-view>
    </div>
</template>
<script>
    export default {
    }
</script>
<style>
    .home {
        margin-top: 60px;
    }

    .home li {
        display: block;
        padding: 15px 25px 15px 25px;
        cursor: pointer;
    }

    .router-link-active {
        background: #e9e9e9;
    }
</style>