<template>
    <div class="home">
        <nav class="navbar navbar-default">
            <div class="container-fluid">
                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">
                        <li class="active"><a href="#">Home <span class="sr-only">(current)</span></a></li>
                        <li><a href="#">Link</a></li>
                        <li><router-link to="/homepage">首页</router-link></li>
                        <li><router-link to="/webpage">web</router-link></li>
                        <li><router-link to="/pythonpage">python</router-link></li>
                        <li><router-link to="/jspage">javascript</router-link></li>
                        <li><router-link to="/htmlpage">html</router-link></li>
                        <li><router-link to="/csspage">css</router-link></li>
                    </ul>
                </div><!-- /.navbar-collapse -->
            </div><!-- /.container-fluid -->
        </nav>
        <router-view></router-view>
    </div>
</template>
<script>
</script>
<style>
    .home {
        margin-top: 60px;
    }
</style>