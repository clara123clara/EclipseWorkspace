package com.lin.baseTest;  
  
import java.util.logging.Logger;

import org.apache.log4j.spi.LoggerFactory;
import org.junit.runner.RunWith;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.AbstractJUnit4SpringContextTests;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;  
//测试基类

/** 
 * 功能概要： 
 *  
 * @author  
 * @since  
 */  
//指定bean注入的配置文件  
@ContextConfiguration(locations = { "classpath:application.xml" })  
//使用标准的JUnit @RunWith注释来告诉JUnit使用Spring TestRunner  
@RunWith(SpringJUnit4ClassRunner.class)  
public abstract class SpringTestCase extends AbstractJUnit4SpringContextTests{  
    protected Logger logger = LoggerFactory.getLogger(getClass());  
}  


