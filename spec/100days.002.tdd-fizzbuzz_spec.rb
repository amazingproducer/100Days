require '100days.002.tdd-fizzbuzz'

RSpec.describe FizzBuzz do
  context "Printing each integer from 1 to 100" do
    it "actually is a range" do
      expect(seed_list.class).to eq(Range)
    end
  end
end


    
