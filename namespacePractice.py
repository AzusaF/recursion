# 以下の PhysicsThings クラスを作成しましょう
# 重力加速度を 9.8 としてください
# 物体の質量を受け取り、重量を返すメソッドを作成してください
# 物体の質量と高さを受け取り、位置エネルギー（質量 * 高さ * 重力加速度）を返すメソッドを作成してください
# 物体の質力と速さを受け取り、運動エネルギー（質量 * 速さ^2 / 2）を返すメソッドを作成してください
class PhysicsThings():
    GRAVITY = 9.8

    def getWeight(mass):
        return PhysicsThings.GRAVITY * mass
    
    def potentialEnergy(mass, height):
        return mass * height * PhysicsThings.GRAVITY
    
    def kineticEnergy(mass, speed):
        return mass * pow(speed, 2) / 2

# 以下のデータを出力してください
# PhysicsThings.GRAVITY - 9.8
# PhysicsThings.getWeight(80) - 784.0
# PhysicsThings.potentialEnergy(80,4) - 3136.0
# PhysicsThings.kineticEnergy(80,10) - 4000.0

print(PhysicsThings.GRAVITY)
print(PhysicsThings.getWeight(80))
print(PhysicsThings.potentialEnergy(80, 4))
print(PhysicsThings.kineticEnergy(80, 10))
